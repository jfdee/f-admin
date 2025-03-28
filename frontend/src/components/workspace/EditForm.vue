<template>
  <el-dialog center :model-value="show">
    <el-input
      style="margin-bottom: 4px"
      v-for="field in writeFields"
      :key="item.name"
      v-model="item[field.name]"
      :placeholder="field.label"
    />
    <div style="display: flex">
      <el-button block @click="onSubmit">+</el-button>
    </div>
  </el-dialog>
</template>

<script>
  export default {
    name: 'EditForm',
    props: {
      show: {
        type: Boolean,
        required: true,
      },
      fields: {
        type: Array,
        required: true,
      },
      row: {
        type: Object,
        default: null,
      },
    },
    data() {
      return {
        item: {},
      }
    },
    watch: {
      row(val) {
        if (!val) return
        this.writeFields.forEach(field => {
          this.item[field.name] = this.row[field.name]
        })
      }
    },
    computed: {
      writeFields() {
        return this.fields.filter(item => !item.read_only)
      },
    },
    methods: {
      onSubmit() {
        this.$emit('submit', this.item)
        this.item = {}
      },
    },
  }
</script>