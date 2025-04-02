<template>
  <el-dialog style="padding-top: 24px" center :model-value="show" @close="onClose">
    <el-alert v-if="alert" class="mb-4" :title="alert" :closable="false" type="error" />
    <el-form
      v-if="isLoaded"
      ref="form"
      :model="item"
      :rules="rules"
      label-position="left"
      label-width="auto"
    >
      <el-form-item v-for="field in fields" :key="field.name" :label="field.label" :prop="field.name">
        <Field v-model="item[field.name]" :meta="field" />
      </el-form-item>
    </el-form>
    <el-skeleton v-else :rows="5" />
    <template #footer>
      <el-row v-if="isLoaded" justify="end">
        <el-button :disabled="isSubmitDisabled" @click="onClose">Cancel</el-button>
        <el-button :disabled="isSubmitDisabled" @click="onSubmit">Submit</el-button>
      </el-row>
    </template>
  </el-dialog>
</template>

<script>
  import Field from './fields/Field.vue'
  export default {
    name: 'CreateForm',
    components: {Field},
    props: {
      apiPath: {
        type: String,
        required: true,
      },
      edit: {
        type: Boolean,
        default: false,
      },
    },
    emits: ['close', 'submit-success'],
    data() {
      return {
        show: false,
        item: {},
        fields: [],
        rules: {},
        alert: null,
        isLoaded: false,
        isSubmitDisabled: false,
      }
    },
    async mounted() {
      this.show = true
      if (!this.edit) {
        await this.load()
        this.setRules()
        this.isLoaded = true
      }
    },
    methods: {
      async load() {
        const promise = this.$ajax.get(`${this.apiPath}meta`)
        promise.then(({data}) => {
          this.fields = data.fields
        })
        return promise
      },
      setRules() {
        const rules = {}
        this.fields.forEach(item => {
          if (!item.required) return
          rules[item.name] = [{required: item.required}]
        })
        this.rules = rules
      },
      onSubmit() {
        this.isSubmitDisabled = true
        this.$refs.form.validate(valid => {
          if (!valid) {
            this.isSubmitDisabled = false
            return
          }
          if (this.edit) {
            this.$emit('submit-success', this.item)
            return
          }
          this.$ajax.post(this.apiPath, this.item).then(() => {
            this.isSubmitDisabled = false
            this.item = {}
            this.$emit('submit-success')
          }).catch(e => {
            this.alert = e.message
          })
        })
      },
      onClose() {
        this.show = false
        this.item = {}
        this.fields = []
        this.rules = {}
        this.$emit('close')
      }
    },
  }
</script>