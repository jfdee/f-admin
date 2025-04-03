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
  import CreateForm from './CreateForm.vue'
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
        this.$refs.form.isLoaded = true
      }
      this.initRowData()
    },
    methods: {
      initRowData() {
        this.$refs.form.fields.forEach(field => {
          let value = this.row[field.name]
          if (field.type === 'related') {
            value = this.row[`${field.name}_id`]
          }
          this.$refs.form.item[field.name] = value
        })
        this.$refs.form.setRules()
      },
      onSubmitSuccess(data) {
        this.$ajax.put(`${this.apiPath}${this.row.id}/`, data).then(() => {
          this.$refs.form.isSubmitDisabled = false
          this.$emit('submit-success')
        }).catch(e => {
          this.$refs.form.alert = e.message
        })
      },
    },
  }
</script>