<template>
  <el-skeleton>
    <template #template>
      <span class="loader" />
    </template>
  </el-skeleton>
</template>

<style scoped>
  .loader {
    width: 64px;
    height: 64px;
    position: absolute;
    top: 50vh;
    left: 50vw;
    background-image: linear-gradient(#01a4f3 16px, transparent 0),
    linear-gradient(#f25313 16px, transparent 0),
    linear-gradient(#84b802 16px, transparent 0),
    linear-gradient(#ffb901 16px, transparent 0);
    background-repeat: no-repeat;
    background-size: 16px 16px;
    background-position: left top, left bottom, right top, right bottom;
    animation: rotate 1s linear infinite;
  }

  @keyframes rotate {
  0% {
    width: 64px;
    height: 64px;
    transform: rotate(0deg)
  }
  50% {
    width: 30px;
    height: 30px;
    transform: rotate(180deg)
  }
  100% {
    width: 64px;
    height: 64px;
    transform: rotate(360deg)
  }
}
</style>
