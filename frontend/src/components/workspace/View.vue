<template>
  <el-container>
    <el-header>
      {{ selectedItem?.label }}
    </el-header>
    <el-main>
      <el-button style="width: 100%" @click="onAdd">+</el-button>
      <el-table class="mt-4" :data="data" border>
        <el-table-column label="edit">
          <template #default="{row}">
            <el-button @click="onEdit(row)">x</el-button>
          </template>
        </el-table-column>
        <el-table-column label="delete">
          <template #default="{row}">
            <el-button @click="onDelete(row)">-</el-button>
          </template>
        </el-table-column>
        <el-table-column
          v-for="field in meta"
          :key="field.name"
          :prop="field.name"
          :label="field.label"
        />
      </el-table>
    </el-main>
    <CreateForm :show="showCreateForm" :fields="meta" @close="showCreateForm=false" @submit="onSubmitCreate" />
    <EditForm :show="showEditForm" :fields="meta" :row="selectedRow" @close="onEditClose" @submit="onSubmitEdit" />
  </el-container>
</template>

<script>
  import MenuStoreMixin from '@/components/MenuStoreMixin'
  import CreateForm from './CreateForm.vue'
  import EditForm from './EditForm.vue'
  export default {
    name: 'MenuItemView',
    components: {CreateForm, EditForm},
    mixins: [MenuStoreMixin],
    data() {
      return {
        data: [],
        meta: [],
        selectedRow: null,
        showCreateForm: false,
        showEditForm: false,
      }
    },
    computed: {
      selectedItem() {
        return this.menuStore.getSelectedItem
      },
    },
    watch: {
      selectedItem() {
        this.load()
      },
    },
    async created() {
      if (!this.menuStore.selected) {
        // page reload
        await this.menuStore.init()
        const code = this.$router.currentRoute.value.params.code
        this.menuStore.setSelected(code)
      }
    },
    methods: {
      load() {
        this.$ajax.get(`/api/admin/menu/${this.selectedItem.code}/`).then(({data}) => {
          this.data = data.data
          this.meta = data.meta
        })
      },
      onAdd() {
        this.showCreateForm = true
      },
      onSubmitCreate(data) {
        this.$ajax.post(`/api/admin/menu/${this.selectedItem.code}/`, data).then(() => {
          this.load()
          this.showCreateForm = false
        })
      },
      onSubmitEdit(data) {
        this.$ajax.put(`/api/admin/menu/${this.selectedItem.code}/${this.selectedRow.id}/`, data).then(() => {
          this.load()
          this.onEditClose()
        })
      },
      onDelete(row) {
        this.$ajax.delete(`/api/admin/menu/${this.selectedItem.code}/${row.id}/`).then(() => {
          this.load()
        })
      },
      onEdit(row) {
        this.selectedRow = row
        this.showEditForm = true
      },
      onEditClose() {
        this.selectedRow = null
        this.showEditForm = false
      },
    },
  }
</script>
