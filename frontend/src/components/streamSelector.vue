<template>
    <div id='stream_selector' class="stream-selector">
        <input v-model="ip">   
        <span></span>
        <button @click='updateIp()'>Update Stream IP</button>
    </div>
</template>

<script >

export default {
  name: 'streamSelector',
  data: () => ({
    ip: ""
  }),
  methods: {
    updateIp: function () {
        this.$emit('updateIp', this.ip);
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.stream-selector {
  position: absolute;
  top: 15%;
  right: 8%;
}
.stream-selector button {
  margin-left: 27px;
}
</style>
