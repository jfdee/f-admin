<template>
  <el-select placeholder="">
    <el-option v-for="[itemId, itemName] of meta.choices" :key="itemId" :label="itemName" :value="itemId" />
  </el-select>
</template>

<script>
  export default {
    name: 'SelectField',
    props: {
      meta: {
        type: Object,
        required: true,
      },
    },
  }
</script>