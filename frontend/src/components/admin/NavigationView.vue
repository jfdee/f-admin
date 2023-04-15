<template>
  <div>
    <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
    >
      <el-menu-item v-for="(item, index) in menuData" :key="index" :index="getValidIndex(index)">
        <el-icon><House /></el-icon>
        <router-link :to="{name: 'components-admin-menu-item-view', params: {code: item.code}}">
            {{ item.label }}
        </router-link>
      </el-menu-item>
    </el-menu>
    <router-view />
  </div>
</template>
<script>

  export default {
    name: 'NavigationView',
    computed: {
      menuData() {
        return [
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
      },
    },
    methods: {
      getValidIndex(value) {
        return String(value)
      },
    },
  }
</script>