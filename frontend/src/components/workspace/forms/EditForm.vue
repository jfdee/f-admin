<template>
  <CreateForm ref="form" :show="show" :fields="fields"/>
</template>

<script>
  import CreateForm from "./CreateForm.vue";
  export default {
    name: 'EditForm',
    components: {CreateForm},
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
    watch: {
      row(val) {
        if (!val) return
        this.$refs.form.writeFields.forEach(field => {
          this.$refs.form.item[field.name] = this.row[field.name]
        })
      }
    },
  }
</script>