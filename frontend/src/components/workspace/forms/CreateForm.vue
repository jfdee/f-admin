<template>
  <el-dialog style="padding-top: 24px" center :model-value="show" @close="onClose">
    <el-form ref="form" :model="item" :rules="rules" label-position="left" label-width="auto">
      <el-form-item v-for="field in writeFields" :key="field.name" :label="field.label" :prop="field.name">
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
    props: {
      show: {
        type: Boolean,
        required: true,
      },
      fields: {
        type: Array,
        required: true,
      },
    },
    data() {
      return {
        item: {},
      }
    },
    computed: {
      writeFields() {
        return this.fields.filter(item => !item.read_only)
      },
      rules() {
        let rules = {}
        this.writeFields.forEach(item => {
          rules[item.name] = [{required: item.required, message: 'Value required', trigger: 'blur'}]
        })
        return rules
      },
    },
    mounted() {
      this.writeFields.forEach(item => {
        this.item[item.name] = null
      })
    },
    methods: {
      onSubmit() {
        this.$refs.form.validate((valid) => {
          if (!valid) return
          this.$emit('submit', this.item)
          this.item = {}
        })
      },
      onClose() {
        this.$refs.form.resetFields()
      }
    },
  }
</script>