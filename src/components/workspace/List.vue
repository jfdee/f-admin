<template>
  <div>
    <el-row class="mb-4" justify="space-between" style="width: 100%">
      <el-pagination layout="prev, pager, next" background :total="count" @current-change="onChangePage" />
      <el-input v-model="search" style="width: 600px" placeholder="Search" />
      <el-button style="width: 130px" title="Create" icon="plus" @click="onCreate" />
    </el-row>
    <el-alert v-if="alert" class="mb-4" :title="alert" :closable="false" type="error" />
    <el-table
      v-show="isLoaded"
      :data="data"
      max-height="700"
      table-layout="auto"
      border
      flexible
    >
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
    <Loader v-show="!isLoaded" />
    <CreateForm
      v-if="showCreateForm"
      :api-path="apiPath"
      @close="onCreateClose"
      @submit-success="onCreateSuccess"
    />
    <EditForm
      v-if="showEditForm"
      :api-path="apiPath"
      :row="selectedRow"
      @close="onEditClose"
      @submit-success="onEditSuccess"
    />
  </div>
</template>

<script>
  import Loader from '@/components/common/Loader.vue'
  import CreateForm from './forms/CreateForm.vue'
  import EditForm from './forms/EditForm.vue'
  export default {
    name: 'List',
    components: {CreateForm, EditForm, Loader},
    props: {
      apiPath: {
        type: String,
        required: true,
      },
    },
    emits: ['loaded'],
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
        isLoaded: false,
        alert: null,
      }
    },
    watch: {
      apiPath() {
        this.page = 1
        this.load()
      },
    },
    created() {
      this.load()
    },
    methods: {
      load() {
        const params = {page: this.page}
        if (this.search) params.search = this.search
        this.isLoaded = false
        this.$ajax.get(this.apiPath, {params}).then(({data}) => {
          this.data = data.data
          this.fields = data.meta.fields.filter(item => item.type !== 'related_id')
          this.count = data.meta.paginator.count
          this.isLoaded = true
          this.$emit('loaded')
        }).catch(e => {
          this.alert = e.message
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
      },
      onEditSuccess() {
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