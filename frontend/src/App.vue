<template>
  <RouterView />
</template>

<script>
  import { RouterView } from 'vue-router'
  export default {
    name: 'App',
    components: {RouterView},
    created() {
      console.log('1')
    },
    mounted() {
      console.log('1')
    },
  }
</script>