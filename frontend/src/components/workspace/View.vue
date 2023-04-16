<template>
  <el-container>
    <el-header>
      {{ selectedItem.label }}
    </el-header>
    <el-main>
      <el-button style="width: 100%" @click="onAdd">Add</el-button>
      <el-table class="mt-4" :data="data" border>
        <el-table-column
          v-for="field in meta"
          :key="field.name"
          :prop="field.name"
          :label="field.label"
        />
      </el-table>
    </el-main>
  </el-container>
</template>

<script>
  import MenuStoreMixin from '/components/MenuStoreMixin'
  export default {
    name: 'MenuItemView',
    mixins: [MenuStoreMixin],
    data() {
      return {
        data: [],
        meta: [],
      }
    },
    computed: {
      selectedItem() {
        return this.menuStore.selected
      },
    },
    async mounted() {
      const {data} = await this.$ajax.get(`/api/admin/items/${this.selectedItem.code}`)
      this.data = data.data
      this.meta = data.meta
    },
    methods: {
      onAdd() {
        console.log('add')
      },
    },
  }
</script>
