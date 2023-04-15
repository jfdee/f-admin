<template>
  <div>{{ code }}</div>
</template>

<script>
  export default {
    name: 'MenuItemView',
    props: {
      code: {
        type: String,
        required: true,
      },
    },
    mounted() {
      console.log(this.code)
    }
  }
</script>
