<template lang="pug">
  .loading
    .middle
      .spinner
        ball-triangle-path-loader(size='20px', color='#23A4CE')
</template>

<script>
export default {
  name: 'loading'
}
</script>

<style lang="sass">
body
  overflow: hidden
  margin: 0px
  background: #13293D

.loading
  display: table
  position: absolute
  height: 100%
  width: 100%

.middle
  display: table-cell
  vertical-align: middle

.spinner
  margin-left: auto
  margin-right: auto
  width: 70px
</style>
