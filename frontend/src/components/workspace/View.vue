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
    <CreateForm :show="showCreateForm" :fields="meta" @close="showCreateForm=false" @submit="onSubmit" />
  </el-container>
</template>

<script>
  import MenuStoreMixin from '/components/MenuStoreMixin'
  import CreateForm from './CreateForm.vue'
  export default {
    name: 'MenuItemView',
    components: {CreateForm},
    mixins: [MenuStoreMixin],
    data() {
      return {
        data: [],
        meta: [],
        showCreateForm: false,
      }
    },
    computed: {
      selectedItem() {
        return this.menuStore.selected
      },
    },
    mounted() {
      this.$ajax.get(`/api/admin/items/${this.selectedItem.code}`).then(({data}) => {
        this.data = data.data
        this.meta = data.meta
      })
    },
    methods: {
      onAdd() {
        this.showCreateForm = true
      },
      onSubmit(data) {
        this.showCreateForm = false
        console.log(data)
      },
    },
  }
</script>
