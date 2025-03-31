<template>
  <CreateForm
    v-if="show"
    ref="form"
    :api-path="apiPath"
    :edit="true"
    @close="$emit('close')"
    @submit-success="onSubmitSuccess"
  />
</template>

<script>
  import CreateForm from "./CreateForm.vue";
  export default {
    name: 'EditForm',
    components: {CreateForm},
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
    emits: ['close', 'submit-success'],
    data() {
      return {
        show: false,
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
          this.$emit('submit-success')
        }).catch(e => {
          console.log(e)
          this.$refs.form.alert = e.message
        })
      },
    },
  }
</script>