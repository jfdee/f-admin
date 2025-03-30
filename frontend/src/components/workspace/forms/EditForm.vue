<template>
  <CreateForm v-if="show" ref="form" :api-path="apiPath" :edit="true" @close="$emit('close')" @submit-success="onSubmitSuccess">
    <template #alert>
      <el-alert v-if="alert" style="margin-bottom: 16px" :title="alert" :closable="false" type="error" />
    </template>
  </CreateForm>
</template>

<script>
  import CreateForm from "./CreateForm.vue";
  export default {
    name: 'EditForm',
    components: {CreateForm},
    emits: ['close', 'submit-success-edit'],
    props: {
      apiPath: {
        type: String,
        required: true,
      },
      row: {
        type: Object,
        default: null,
      },
    },
    data() {
      return {
        show: false,
        alert: null,
      }
    },
    created() {
      this.show = true
    },
    async mounted() {
      if (!this.$refs.form.fields.length) {
        await this.$refs.form.load()
      }
      this.initRowData()
    },
    methods: {
      initRowData() {
        this.$refs.form.fields.forEach(field => {
          this.$refs.form.item[field.name] = this.row[field.name]
        })
        this.$refs.form.setRules()
      },
      onSubmitSuccess(data) {
        this.$ajax.put(`${this.apiPath}${this.row.id}/`, data).then(() => {
          this.$emit('submit-success-edit')
        }).catch(e => {
          console.log(e)
          this.alert = e.message
        })
      },
    },
  }
</script>