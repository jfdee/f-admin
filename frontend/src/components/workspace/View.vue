<template>
  <el-container>
    <el-header>
      {{ modelMeta.label }}
    </el-header>
    <el-main>
      <el-button style="width: 100%" @click="onAdd">Add</el-button>
      <el-table class="mt-4" :data="tableData" border>
        <el-table-column
          v-for="field in modelMeta.fields"
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
    computed: {
      modelMeta() {
        return this.menuStore.selected
      },
      tableData() {
        return [
          {
            'field1': 'f_value1.1',
            'field2': 'f_value1.2',
            'field3': 'f_value1.3',
            'field4': 'f_value1.4',
          },
          {
            'field1': 'f_value2.1',
            'field2': 'f_value2.2',
            'field3': 'f_value2.3',
            'field4': 'f_value2.4',
          },
        ]
      },
    },
    methods: {
      onAdd() {
        console.log('add')
      },
    },
  }
</script>
