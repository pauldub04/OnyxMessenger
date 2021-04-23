<template>
  <v-app>
    <v-text-field v-model="message" label="message"></v-text-field>
    <div v-for="(m, i) in messages" v-bind:key="i">{{ m.message }}</div>

    <v-btn @click="send">send</v-btn>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    websocket: null,
    message: null,
    messages: [],
  }),
  created() {
    // adsf
  },
  mounted() {
    this.connectToWebSocket()
  },
  methods: {
    send() {
      this.websocket.send(
        JSON.stringify({
          message: this.message,
        })
      )
    },
    connectToWebSocket() {
      this.websocket = new WebSocket('ws://127.0.0.1:8000/ws/chat/kek/')
      this.websocket.onopen = this.onOpen
      this.websocket.onclose = this.onClose
      this.websocket.onmessage = this.onMessage
      this.websocket.onerror = this.onError
    },
    onOpen(event) {
      console.log('Connection opened.', event.data)
    },
    onClose(event) {
      console.log('Connection closed.', event.data)
    },
    onMessage(event) {
      const message = JSON.parse(event.data)
      this.messages.push(message)
      console.log(message)
    },
    onError(event) {
      alert('An error occured:', event.data)
    },
  },
}
</script>
