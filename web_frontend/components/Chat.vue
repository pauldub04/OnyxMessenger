<template>
  <v-main>
    <v-toolbar id="info-bar" ref="infoBar" flat dark>
      <v-badge bordered bottom color="green" dot offset-x="16" offset-y="9">
        <v-avatar class="mr-2" size="40" elevation="10">
          <v-img :src="context.userImage" />
        </v-avatar>
      </v-badge>
      <v-toolbar-title class="ma-2" v-if="showUsersCount % 2 == 0">
        {{ context.title }}
      </v-toolbar-title>
      <!-- <v-card
        class="mx-auto mt-10"
        max-width="400"
        tile
        v-if="showUsersCount % 2 == 1"
      >
        <v-list-item two-line v-for="(user, i) in members" v-bind:key="i">
          <v-list-item-content>
            <v-list-item-title> {{ user.username }} </v-list-item-title>
            <v-list-item-subtitle v-if="user.type == 'owner'">
              owner
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-card>
      <v-btn depressed icon small @click="showUsersCount++">
        <v-icon v-if="showUsersCount % 2 == 0"> mdi-menu-down </v-icon>
        <v-icon v-else> mdi-menu-up </v-icon>
      </v-btn> -->

      <v-spacer></v-spacer>
      <v-toolbar-items>
        <!-- <v-text-field
          v-if="inviteCount % 2 == 1"
          v-model="inviteUserName"
          class="mt-4 mr-5"
          label="Добавить пользователя"
          placeholder="Введите username"
          append-outer-icon="mdi-plus"
          clearable
          @click:append-outer="invite"
        >
        </v-text-field> -->
        <v-autocomplete
          chips
          deletable-chips
          multiple
          :items="users"
          v-if="inviteCount % 2 == 1"
          v-model="inviteUserName"
          class="mt-4 mr-5"
          placeholder="Введите username"
          clearable
          append-outer-icon="mdi-send"
          @click:append-outer="invite"
          label="Добавить пользователя"
        ></v-autocomplete>
        <v-btn icon fab dark small @click="toInvite"
          ><v-icon>{{ icons.accountPlus }}</v-icon>
        </v-btn>
        <v-btn icon fab dark small
          ><v-icon>{{ icons.searchIcon }}</v-icon></v-btn
        >
        <v-btn icon fab dark small
          ><v-icon>{{ icons.chatInfo }}</v-icon></v-btn
        >
        <!-- <v-menu offset-y>
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" icon fab dark small v-on="on">
              <v-icon>{{ icons.extraInfo }}</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item
              v-for="(item, index) in itemsDropdownMenu"
              :key="index"
            >
              <v-list-item-title> {{ item.title }} </v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu> -->
      </v-toolbar-items>
    </v-toolbar>
    <v-divider></v-divider>
    <v-list id="messageContainer" :height="height" class="overflow-y-auto dark">
      <v-list-item v-for="(message, index) in context.messages" :key="index">
        <v-app-bar
          v-if="message.user.id === $store.state.user.id"
          color="rgba(0,0,0,0)"
          flat
          :class="index === context.messages.length ? 'mb-15 mt-15' : 'mb-15'"
        >
          <v-spacer></v-spacer>
          <v-card class="mt-16 mr-2" max-width="350px" color="blue" dark>
            <v-list-item three-line>
              <v-list-item-content>
                <div class="mb-4">
                  <h3>{{ message.user.username }}</h3>
                </div>
                <div>
                  {{ message.message }}
                </div>
              </v-list-item-content>
            </v-list-item>
          </v-card>
          <v-badge
            bordered
            bottom
            color="green"
            dot
            offset-x="10"
            offset-y="10"
          >
            <v-avatar class="mt-n5" size="30" elevation="10">
              <v-img src="https://cdn.vuetifyjs.com/images/lists/5.jpg" />
            </v-avatar>
          </v-badge>
        </v-app-bar>
        <v-app-bar
          v-else
          color="rgba(0,0,0,0)"
          flat
          :class="index === context.messages.length ? 'mb-15 mt-15' : 'mb-15'"
        >
          <v-badge bordered bottom color="green" dot offset-x="16" offset-y="9">
            <v-avatar class="mt-n5 mr-2" size="30" elevation="10">
              <v-img :src="context.userImage" />
            </v-avatar>
          </v-badge>
          <v-card class="mt-10" max-width="350px" color="grey">
            <v-list-item three-line>
              <v-list-item-content>
                <div class="mb-4">
                  <h3>{{ message.user.username }}</h3>
                </div>
                <div>
                  {{ message.message }}
                </div>
              </v-list-item-content>
            </v-list-item>
          </v-card>
        </v-app-bar>
      </v-list-item>
      <v-btn
        :hidden="checkIsDown"
        style="background-color: grey"
        large
        icon
        bottom
        right
        absolute
        class="mr-2 mb-16"
        @click="scrollToBottom"
      >
        <v-icon>{{ icons.down }}</v-icon>
      </v-btn>
    </v-list>
    <v-divider></v-divider>
    <v-overlay v-model="overlay" :z-index="zIndex">
      <VEmojiPicker
        v-click-outside="onClickOutsideEmojiPicker"
        class="align-center justify-center"
        @select="selectEmoji"
      ></VEmojiPicker>
    </v-overlay>
    <v-app-bar id="input-form" ref="inputForm" color="rgba(0,0,0,0)" flat>
      <upload-btn
        noTitleUpdate
        class="pa-0"
        multiple
        hover
        icon
        flat
        round
        small
        depressed
        maxWidth="15"
        @file-update="updateFile"
      >
        <template slot="icon">
          <v-icon>{{ icons.attach }}</v-icon>
        </template>
      </upload-btn>
      <v-text-field v-model="message" class="mt-6" @keyup.enter="sendMessage">
      </v-text-field>
      <v-btn icon @click="overlay = !overlay">
        <v-icon>{{ icons.smile }}</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon @click="messageOrAudio">
          {{ message ? icons.send : icons.micro }}
        </v-icon>
      </v-btn>
    </v-app-bar>
  </v-main>
</template>

<script>
/* eslint-disable */
import {
  mdiMagnify,
  mdiPageLayoutSidebarRight,
  mdiDotsVertical,
  mdiPaperclip,
  mdiEmoticonHappyOutline,
  mdiMicrophoneOutline,
  mdiSend,
  mdiCloseCircle,
  mdiPlus,
  mdiAccountPlus,
  mdiChevronDown,
} from '@mdi/js'
import { VEmojiPicker } from 'v-emoji-picker'
// import UploadButton from 'vuetify-upload-button'
export default {
  name: 'Chat',
  components: {
    // eslint-disable-next-line vue/no-unused-components
    VEmojiPicker,
    // 'upload-btn': UploadButton
  },
  props: {
    context: {
      type: Object,
      default: null,
    },
  },
  data: () => ({
    message: '',
    user_id: 1,
    height: 0,
    overlay: false,
    zIndex: 0,
    icons: {
      searchIcon: mdiMagnify,
      chatInfo: mdiPageLayoutSidebarRight,
      extraInfo: mdiDotsVertical,
      attach: mdiPaperclip,
      smile: mdiEmoticonHappyOutline,
      micro: mdiMicrophoneOutline,
      send: mdiSend,
      closeCircle: mdiCloseCircle,
      plus: mdiPlus,
      accountPlus: mdiAccountPlus,
      down: mdiChevronDown,
    },
    files: [],
    itemsDropdownMenu: [],
    showUsersCount: 0,
    inviteCount: 0,
    inviteUserName: null,
    users: [],
  }),
  watch: {},
  created() {
    // setInterval(this.getMessages, 3000)
  },
  mounted() {
    this.getUsers()
    this.getMessages()
    this.connectToWebSocket()

    this.scrollToBottom()
    this.checkIsDown()

    this.$nextTick(function () {
      this.matchHeight()
      this.checkIsDown()
    })
    window.addEventListener('resize', this.matchHeight)
    window.addEventListener('resize', this.checkIsDown)
  },
  computed() {
    checkIsDown()
  },
  methods: {
    connectToWebSocket() {
      this.websocket = new WebSocket(
        `ws://127.0.0.1:8000/ws/chat/${this.context.uri}/`,
        this.$store.getters.getToken
      )
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
      console.log(this.$el.querySelector('#messageContainer').scrollHeight)
      console.log(this.$el.querySelector('#messageContainer').scrollTopMax)
      console.log(this.$el.querySelector('#messageContainer').scrollTop)
      if (
        this.$el.querySelector('#messageContainer').scrollTop ===
        this.$el.querySelector('#messageContainer').scrollTopMax
      ) {
        setTimeout(() => {
          this.scrollToBottom(), 2000
        })
      }
      this.context.messages.push(message.message)
      this.context.lastMessage = message.message.message
      console.log(message.message)
    },
    onError(event) {
      alert('An error occured:', event.data)
    },

    // ----------------------------------------------------
    checkIsDown() {
      return this.$el.querySelector('#messageContainer').scrollTop === this.$el.querySelector('#messageContainer').scrollTopMax
    },

    scrollToBottom() {
      const container = this.$el.querySelector('#messageContainer')
      container.scrollTop = container.scrollTopMax
    },
    toInvite() {
      this.inviteCount++
    },
    invite() {
      if (this.inviteUserName !== null) {
        console.log(this.inviteUserName)

        for (let username of this.inviteUserName)
          this.$axios
            .patch(`http://127.0.0.1:8000/api/chats/${this.context.uri}/`, {
              username: username,
            })
            .then((response) => {
              // console.log(response.data)
              alert(response.data.message)
            })
            .catch((error) => {
              console.log(error)
            })

        this.inviteCount++
        this.inviteUserName = null
        this.getMessages()
      }
    },
    updateFile(file) {
      this.files.push(file)
      console.log('File in files!')
    },
    getUsers() {
      this.$axios
        .get(`http://127.0.0.1:8000/api/users/all/`)
        .then((response) => {
          this.users = response.data.users
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMessages() {
      this.$axios
        .get(`http://localhost:8000/api/chats/${this.context.uri}/messages/`)
        .then((response) => {
          console.log(response.data)

          this.members = response.data.members
          this.context.messages = response.data.messages
          if (response.data.messages.length != 0)
            this.context.lastMessage =
              response.data.messages[response.data.messages.length - 1].message
          // console.log(this.context.messages)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    matchHeight() {
      const heightInfobar = document.getElementById('info-bar').offsetHeight
      const heightForm = document.getElementById('input-form').offsetHeight
      const windowHeight = window.innerHeight
      this.height = windowHeight - (heightInfobar + heightForm) - 2
    },
    attachFile() {
      alert('File attached')
    },
    clearMessage() {
      this.message = ''
    },
    messageOrAudio() {
      if (this.message) {
        this.sendMessage()
      } else {
        this.makeAudioMessage()
      }
    },
    sendMessage() {
      if (this.message == null || this.message == '') return
      this.websocket.send(
        JSON.stringify({
          message: this.message,
          user: this.$store.getters.getUser,
          uri: this.context.uri,
        })
      )
      // this.$axios
      //   .post(`http://localhost:8000/api/chats/${this.context.uri}/messages/`, {
      //     message: this.message,
      //   })
      //   .then((response) => {
      //     console.log(response.data)
      //     this.getMessages()
      //   })
      //   .catch((error) => {
      //     console.log(error)
      //   })
      this.clearMessage()
      // this.scrollToBottom()
    },
    makeAudioMessage() {
      alert('Audio done!')
    },
    selectEmoji(emoji) {
      this.message += emoji.data
    },
    onClickOutsideEmojiPicker() {
      this.overlay = false
    },
  },
}
</script>

<style>
.v-btn--example {
  bottom: 10;
  position: absolute;
  margin: 0 0 80px 150px;
}
</style>
