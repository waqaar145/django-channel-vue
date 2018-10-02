<template>
  <div class="hello">
    <ul>
      <li v-for="chat in chats" :key="chat">
        {{chat}} by waqaar
      </li>
      <input type="text" v-model="message"/>
      <button type="submit" v-on:click="sendMessage()">click me</button>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      message: '',
      chatSocket: {},
      chats: []
    }
  },
  mounted () {
    console.log(this.chats)
    var loc = window.location
    var path = loc.pathname
    var tes = this.chats
    this.chatSocket = new WebSocket('ws://' + '10.0.0.2:8000' + '/ws/chat' + path + '/')
    this.chatSocket.onmessage = function (e) {
      console.log('on message', e)
      let message = JSON.parse(e.data)
      console.log(message.message)
      console.log(tes)
    }

    this.chatSocket.onclose = function (e) {
      console.log('on close', e)
    }

    this.chatSocket.onerror = function (e) {
      console.log('on receive', e)
    }

    this.chatSocket.onopen = function (e) {
      console.log('on open', e)
    }
  },
  methods: {
    sendMessage () {
      console.log('being clicked')
      let finalData = {
        'message': this.message
      }
      this.chatSocket.send(JSON.stringify(finalData))
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
