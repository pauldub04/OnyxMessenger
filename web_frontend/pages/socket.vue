<template>
  <v-app>
    <v-text-field v-model="message" label="message"></v-text-field>
    <v-btn @click="send">send</v-btn>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    chatSocket: null,
    message: null,
  }),
  mounted() {
    this.chatSocket = new WebSocket('ws://127.0.0.1:8000/ws/chat/lobby/')

    this.chatSocket.onmessage = function (e) {
      const data = JSON.parse(e.data)
      console.log(data.message)
    }

    this.chatSocket.onclose = function (e) {
      console.error('Chat socket closed unexpectedly')
    }
  },
  methods: {
    send() {
      this.chatSocket.send(
        JSON.stringify({
          message: this.message,
        })
      )
    },
  },
}
</script>
