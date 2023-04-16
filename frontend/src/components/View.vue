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
    async mounted() {
      const {data} = await this.$ajax.get('/api/admin/items')
      this.menuStore.items = data
    },
  }
</script>
