<template>
  <el-container>
    <el-header>
      {{ menuItem.label }}
    </el-header>
    <el-main>
      {{ menuItem.code }}
    </el-main>
  </el-container>
</template>

<script>
  import MenuStoreMixin from '/components/MenuStoreMixin'
  export default {
    name: 'MenuItemView',
    mixins: [MenuStoreMixin],
    computed: {
      menuItem() {
        return this.menuStore.selected
      },
    },
  }
</script>
