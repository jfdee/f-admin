<template>
  <el-container v-if="selectedItem">
    <el-header height="fit-content">
      {{ selectedItem.label }}
    </el-header>
    <el-main>
      <el-row justify="space-between" style="margin-bottom: 12px; width: 100%">
        <el-pagination layout="prev, pager, next" background :total="count" @current-change="onChangePage" />
        <el-button style="width: 130px" title="Create" icon="plus" @click="onCreate" />
      </el-row>
      <el-table :data="data" max-height="700" table-layout="auto" border flexible>
        <el-table-column width="130">
          <template #default="{row}">
            <el-button title="Edit" icon="edit" @click="onEdit(row)" />
            <el-button title="Delete" icon="delete" @click="onDelete(row)" />
          </template>
        </el-table-column>
        <el-table-column
          v-for="field in fields"
          :key="field.name"
          :prop="field.name"
          :label="field.label"
          show-overflow-tooltip
          min-width="130"
        />
      </el-table>
    </el-main>
    <CreateForm :show="showCreateForm" :fields="fields" @close="onCreateClose" @submit="onSubmitCreate" />
    <EditForm :show="showEditForm" :fields="fields" :row="selectedRow" @close="onEditClose" @submit="onSubmitEdit" />
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
        fields: [],
        selectedRow: null,
        showCreateForm: false,
        showEditForm: false,
        page: 1,
        count: 0,
      }
    },
    computed: {
      selectedItem() {
        return this.menuStore.getSelectedItem
      },
    },
    watch: {
      selectedItem(val, oldVal) {
        this.page = 1
        if (oldVal === undefined) return
        this.load()
      },
    },
    async created() {
      if (!this.menuStore.selected) {
        // page reload12
        await this.menuStore.init()
        const code = this.$router.currentRoute.value.params.code
        this.menuStore.setSelected(code)
      }
      this.load()
    },
    methods: {
      load() {
        const params = {page: this.page}
        this.$ajax.get(`/api/admin/menu/${this.selectedItem.code}/`, {params}).then(({data}) => {
          this.data = data.data
          this.fields = data.meta.fields
          this.count = data.meta.paginator.count
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
          this.showCreateForm = false
          this.page = 1
          this.load()
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
      onChangePage(page) {
        this.page = page
        this.load()
      },
    },
  }
</script>
