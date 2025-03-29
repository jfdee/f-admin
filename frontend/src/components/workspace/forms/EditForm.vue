<template>
  <el-dialog center :model-value="show">
    <el-form :model="item" label-position="left" label-width="auto">
      <el-form-item v-for="field in writeFields" :key="field.name" :label="field.label">
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
    name: 'EditForm',
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
      row: {
        type: Object,
        default: null,
      },
    },
    data() {
      return {
        item: {},
      }
    },
    watch: {
      row(val) {
        if (!val) return
        this.writeFields.forEach(field => {
          this.item[field.name] = this.row[field.name]
        })
      }
    },
    computed: {
      writeFields() {
        return this.fields.filter(item => !item.read_only)
      },
    },
    methods: {
      onSubmit() {
        this.$emit('submit', this.item)
        // this.item = {}
      },
    },
  }
</script>