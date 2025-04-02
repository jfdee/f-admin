<template>
  <component :is="component" :meta="meta" />
</template>

<script>
  import BooleanField from './BooleanField.vue'
  import DateField from './DateField.vue'
  import DateTimeField from './DateTimeField.vue'
  import TextField from './TextField.vue'
  import NumberField from './NumberField.vue'
  import SelectField from './SelectField.vue'
  export default {
    name: 'FieldView',
    props: {
      meta: {
        type: Object,
        required: true,
      },
    },
    data() {
      return {
        value: null,
      }
    },
    computed: {
      component() {
        switch (this.meta.type) {
          case 'bool':
            return BooleanField
          case 'int':
            return NumberField
          case 'date':
            return DateField
          case 'datetime':
            return DateTimeField
          case 'related':
            return SelectField
          default:
            return TextField
        }
      },
    },
  }
</script>