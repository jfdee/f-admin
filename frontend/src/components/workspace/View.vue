<template>
  <el-container v-if="selectedItem">
    <el-header>
      {{ selectedItem.label }}
    </el-header>
    <el-main>
      <el-row justify="end" style="margin-bottom: 12px">
        <el-button style="width: 130px" title="Create" icon="plus" @click="onCreate" />
      </el-row>
      <el-table :data="data" border table-layout="auto">
        <el-table-column
          v-for="field in meta"
          :key="field.name"
          :prop="field.name"
          :label="field.label"
        />
        <el-table-column width="130">
          <template #default="{row}">
            <el-button title="Edit" icon="edit" @click="onEdit(row)" />
            <el-button title="Delete" icon="delete" @click="onDelete(row)" />
          </template>
        </el-table-column>
      </el-table>
    </el-main>
    <CreateForm :show="showCreateForm" :fields="meta" @close="onCreateClose" @submit="onSubmitCreate" />
    <EditForm :show="showEditForm" :fields="meta" :row="selectedRow" @close="onEditClose" @submit="onSubmitEdit" />
  </el-container>
</template>

<script>
  import MenuStoreMixin from '@/components/MenuStoreMixin'
  import CreateForm from './forms/CreateForm.vue'
  import EditForm from './forms/EditForm.vue'
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
      this.load()
    },
    methods: {
      load() {
        this.$ajax.get(`/api/admin/menu/${this.selectedItem.code}/`).then(({data}) => {
          this.data = data.data
          this.meta = data.meta
        })
      },
      onCreate() {
        this.showCreateForm = true
      },
      onCreateClose() {
        this.showCreateForm = false
      },
      onSubmitCreate(data) {
        this.$ajax.post(`/api/admin/menu/${this.selectedItem.code}/`, data).then(() => {
          this.load()
          this.showCreateForm = false
        }).catch(e => {
          console.log(e)
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
      onSubmitEdit(data) {
        this.$ajax.put(`/api/admin/menu/${this.selectedItem.code}/${this.selectedRow.id}/`, data).then(() => {
          this.load()
          this.onEditClose()
        }).catch(e => {
          console.log(e)
        })
      },
      onDelete(row) {
        this.$ajax.delete(`/api/admin/menu/${this.selectedItem.code}/${row.id}/`).then(() => {
          this.load()
        }).catch(e => {
          console.log(e)
        })
      },
    },
  }
</script>
