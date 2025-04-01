<template>
  <el-container>
    <el-header height="fit-content">{{ selectedItem.label }}</el-header>
    <el-main>
      <Loader v-show="!isLoaded" />
      <List v-show="isLoaded" :api-path="apiPath" @loaded="isLoaded = true" />
    </el-main>
  </el-container>
</template>

<script>
  import MenuStoreMixin from '@/components/common/MenuStoreMixin'
  import Loader from '@/components/common/Loader.vue'
  import List from './List.vue'

  export default {
    name: 'MenuItemView',
    components: {Loader, List},
    mixins: [MenuStoreMixin],
    data() {
      return {
        isLoaded: false,
      }
    },
    computed: {
      selectedItem() {
        return this.menuStore.getSelectedItem
      },
      apiPath() {
        return `/api/admin/menu/${this.selectedItem.code}/`
      },
    },
    watch: {
      selectedItem() {
        // Включаем общий лоадер, если поменялся был переход в другой пункт меню
        this.isLoaded = false
      },
    },
  }
</script>
