<template>
  <div>
    <LoaderView v-if="isLoading" />
    <el-container v-else>
      <el-aside width="200px">
        <NavigationView />
      </el-aside>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </div>
</template>

<script>
  import MenuStoreMixin from '@/components/MenuStoreMixin'
  import NavigationView from './navigation/View.vue'
  import LoaderView from './LoaderView.vue'
  export default {
    name: 'AdminView',
    components: {NavigationView, LoaderView},
    mixins: [MenuStoreMixin],
    data() {
      return {
        isLoading: false,
      }
    },
    async created() {
      this.isLoading = true
      await this.menuStore.init()
      if (this.$router.currentRoute.value.params.code !== undefined) {
        const code = this.$router.currentRoute.value.params.code
        this.menuStore.setSelected(code)
      }
      this.isLoading = false
      // TODO(в else проставить this.menuStore.setSelected(router.params.code))
    },
  }
</script>
