<template>
  <div>
    <Loader v-if="!isLoaded" />
    <el-container v-else>
      <el-aside>
        <NavigationView />
      </el-aside>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </div>
</template>

<script>
  import MenuStoreMixin from '@/components/common/MenuStoreMixin'
  import Loader from '@/components/common/Loader.vue'
  import NavigationView from './navigation/View.vue'
  export default {
    name: 'AdminView',
    components: {NavigationView, Loader},
    mixins: [MenuStoreMixin],
    data() {
      return {
        isLoaded: false,
      }
    },
    created() {
      this.load()
    },
    methods: {
      async load() {
        this.isLoaded = false
        await this.menuStore.init()
        const code = this.$router.currentRoute.value.params.code
        if (code !== undefined) {
          this.menuStore.setSelected(code)
        }
        this.isLoaded = true
      },
    },
  }
</script>
