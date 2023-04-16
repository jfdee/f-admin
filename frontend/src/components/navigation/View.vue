<template>
  <el-menu
    default-active="2"
    class="el-menu-vertical-demo"
  >
    <el-menu-item
      v-for="(item, index) in menuItems"
      :key="index"
      :index="getValidIndex(index)"
      @click="onSelectItem(item)"
    >
      <el-icon><House /></el-icon>
      <span>{{ item.label }}</span>
    </el-menu-item>
  </el-menu>
</template>
<script>
  import MenuStoreMixin from '/components/MenuStoreMixin'
  export default {
    name: 'NavigationView',
    mixins: [MenuStoreMixin],
    computed: {
      menuItems() {
        return this.menuStore.items
      },
    },
    methods: {
      getValidIndex(value) {
        return String(value)
      },
      onSelectItem(item) {
        this.menuStore.selected = item
        this.$router.push({name: 'components-admin-menu-item-view', params: {code: item.code}})
      },
    },
  }
</script>