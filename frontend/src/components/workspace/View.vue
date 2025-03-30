<template>
  <LoaderView v-if="!isPageLoaded" />
  <el-container v-if="isPageLoaded && selectedItem">
    <el-header height="fit-content">
      {{ selectedItem.label }}
    </el-header>
    <el-main>
      <el-row justify="space-between" style="margin-bottom: 12px; width: 100%">
        <el-pagination layout="prev, pager, next" background :total="count" @current-change="onChangePage" />
        <el-input v-model="search" style="width: 600px" placeholder="Search" />
        <el-button style="width: 130px" title="Create" icon="plus" @click="onCreate" />
      </el-row>
      <LoaderView v-show="!isTableLoaded" />
      <el-table v-show="isTableLoaded" :data="data" max-height="700" table-layout="auto" border flexible>
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
    <CreateForm v-if="showCreateForm" :api-path="apiPath" @close="onCreateClose" @submit-success="onCreateSuccess" />
    <EditForm v-if="showEditForm" :api-path="apiPath" :row="selectedRow" @close="onEditClose" @submit-success-edit="onEditSuccess" />
  </el-container>
</template>

<script>
import MenuStoreMixin from '@/components/MenuStoreMixin'
import LoaderView from '@/components/LoaderView.vue'
import CreateForm from './forms/CreateForm.vue'
import EditForm from './forms/EditForm.vue'

export default {
  name: 'MenuItemView',
  components: {CreateForm, EditForm, LoaderView},
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
      search: null,
      isPageLoaded: false,
      isTableLoaded: false,
    }
  },
  computed: {
    selectedItem() {
      return this.menuStore.getSelectedItem
    },
    apiPath() {
      return `/api/admin/menu/${this.selectedItem.code}/`
    },
  },
  watch: {
    selectedItem(val, oldVal) {
      if (oldVal === undefined) return
      this.page = 1
      this.isPageLoaded = false
      this.load()
    },
    // На бекенде проблема с пагинацией, поэтому пока отключаем
    // search() {
    // this.page = 1
    // this.load()
    // },
  },
  created() {
    this.load()
  },
  methods: {
    load() {
      const params = {page: this.page}
      if (this.search) params.search = this.search
      this.isTableLoaded = false
      this.$ajax.get(this.apiPath, {params}).then(({data}) => {
        this.data = data.data
        this.fields = data.meta.fields
        this.count = data.meta.paginator.count
        this.isTableLoaded = true
        this.isPageLoaded = true
      })
    },
    onCreate() {
      this.showCreateForm = true
    },
    onCreateClose() {
      this.showCreateForm = false
    },
    onCreateSuccess() {
      this.showCreateForm = false
      this.page = 1
      this.load()
    },
    onEdit(row) {
      this.selectedRow = row
      this.showEditForm = true
    },
    onEditClose() {
      this.selectedRow = null
      this.showEditForm = false
      console.log('onEditClose')
    },
    onEditSuccess() {
      console.log('onEditSuccess')
      this.onEditClose()
      this.load()
    },
    onDelete(row) {
      this.$ajax.delete(`${this.apiPath}${row.id}/`).then(() => {
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
