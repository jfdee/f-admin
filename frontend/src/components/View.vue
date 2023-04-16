<template>
  <el-container>
    <el-aside width="200px">
      <NavigationView />
    </el-aside>
    <el-main>
      <router-view />
    </el-main>
  </el-container>
</template>

<script>
  import MenuStoreMixin from '/components/MenuStoreMixin'
  import NavigationView from './navigation/View.vue'
  export default {
    name: 'AdminView',
    components: {NavigationView},
    mixins: [MenuStoreMixin],
    mounted() {
      const items = [
        {
          id: 1,
          'code': 'first-model',
          'label': 'First model',
        },
        {
          id: 2,
          'code': 'second-model',
          'label': 'Second model',
        },
      ]
      this.menuStore.items = items
    },
  }
</script>
