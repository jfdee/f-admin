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
      this.menuStore.items = [
        {
          id: 1,
          code: 'first-model',
          label: 'first model',
          fields: [
            {name: 'field1', label: '1 field'},
            {name: 'field2', label: '2 field'},
          ],
        },
        {
          id: 2,
          code: 'second-model',
          label: 'second model',
          fields: [
            {name: 'field1', label: '1 field'},
            {name: 'field2', label: '2 field'},
            {name: 'field3', label: '3 field'},
          ],
        },
        {
          id: 3,
          code: 'third-model',
          label: 'third model',
          fields: [
            {name: 'field1', label: '1 field'},
            {name: 'field2', label: '2 field'},
            {name: 'field3', label: '3 field'},
            {name: 'field4', label: '4 field'},
          ],
        },
      ]
    },
  }
</script>
