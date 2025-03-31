<template>
  <el-dialog style="padding-top: 24px" center :model-value="show" @close="onClose">
    <el-alert v-if="alert" class="mb-4" :title="alert" :closable="false" type="error" />
    <el-form ref="form" :model="item" :rules="rules" label-position="left" label-width="auto">
      <el-form-item v-for="field in fields" :key="field.name" :label="field.label" :prop="field.name">
        <Field v-model="item[field.name]" :meta="field"/>
      </el-form-item>
    </el-form>
    <template #footer>
      <el-row justify="end">
        <el-button @click="onSubmit">Submit</el-button>
      </el-row>
    </template>
  </el-dialog>
</template>

<script>
  import Field from './components/Field.vue'
  export default {
    name: 'CreateForm',
    components: {Field},
    emits: ['close', 'submit-success'],
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
    data() {
      return {
        show: false,
        item: {},
        fields: [],
        rules: {},
        alert: null,
      }
    },
    async created() {
      if (this.edit) return
      await this.load()
      this.setRules()
      this.show = true
    },
    mounted() {
      if (this.edit) {
        this.show = true
      }
    },
    methods: {
      async load() {
        return this.$ajax.get(`${this.apiPath}meta`).then(({data}) => {
          this.fields = data.fields
        })
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
        this.$refs.form.validate(valid => {
          if (!valid) return
          if (this.edit) {
            this.$emit('submit-success', this.item)
            return
          }
          this.$ajax.post(this.apiPath, this.item).then(() => {
            this.item = {}
            this.$emit('submit-success')
          }).catch(e => {
            console.log(e.message)
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