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
    name: 'CreateForm',
    props: {
      show: {
        type: Boolean,
        required: true,
      },
      fields: {
        type: Array,
        required: true,
      },
    },
    data() {
      return {
        item: {},
      }
    },
    computed: {
      writeFields() {
        return this.fields.filter(item => !item.read_only)
      },
    },
    mounted() {
      this.writeFields.forEach(item => {
        this.item[item.name] = null
      })
    },
    methods: {
      onSubmit() {
        this.$emit('submit', this.item)
      },
    },
  }
</script>