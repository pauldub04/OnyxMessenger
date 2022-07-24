<!-- eslint-disable -->
<template>
  <v-main>
    <v-toolbar id="info-bar" ref="infoBar" flat>
      <!-- <v-badge bordered bottom color="green" dot offset-x="16" offset-y="9">
        <v-avatar class="mr-2" size="40" elevation="10">
          <v-img :src="'http://localhost:8000/media/' + context.image" />
        </v-avatar>
      </v-badge> -->
      <v-avatar
        v-if="context.image !== 'null'"
        class="mr-2"
        size="40"
        elevation="10"
      >
        <v-img :src="'http://localhost:8000/media/' + context.image" />
      </v-avatar>
      <v-row @click="printUsers">
        <v-toolbar-title v-if="showUsersCount % 2 == 0" class="ma-2 ml-5">
          {{ context.title }}
        </v-toolbar-title>
        <v-dialog v-model="showSettings" width="500">
          <template v-slot:activator="{ on, attrs }">
            <v-btn icon small v-bind="attrs" class="mt-2 ml-2" v-on="on">
              <v-icon> mdi-account </v-icon>
            </v-btn>
          </template>

          <v-card>
            <v-card-title class="headline"> {{ context.title }} </v-card-title>

            <v-card-text v-for="(m, i) in context.members" :key="i" class="ma-0 py-1">
              {{ m.username }}
            </v-card-text>

            <v-divider light class="mx-4 mt-3"></v-divider>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" text @click="showSettings = false">
                {{ $t('close') }}
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>

      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-autocomplete
          v-if="inviteCount % 2 == 1"
          v-model="inviteUserName"
          chips
          deletable-chips
          multiple
          :items="users"
          class="mt-4 mr-5"
          clearable
          append-outer-icon="mdi-send"
          :label="$t('pages.createChat.stepTwo.placeholderTwo')"
          @click:append-outer="invite"
        ></v-autocomplete>
        <v-btn icon fab small @click="toInvite"
          ><v-icon>{{ icons.accountPlus }}</v-icon>
        </v-btn>
        <v-btn icon fab small
          ><v-icon>{{ icons.searchIcon }}</v-icon></v-btn
        >
        <v-btn icon fab small
          ><v-icon>{{ icons.chatInfo }}</v-icon></v-btn
        >
        <!-- <v-menu offset-y>
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" icon fab  small v-on="on">
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

    <v-divider light></v-divider>
    
    <v-list id="messageContainer" :height="height" class="overflow-y-auto">
      <v-list-item v-for="(message, index) in context.messages" :key="index">

        <v-row v-if="message.user.id === $store.state.user.id"
          :class="index === context.messages.length-1 ? 'ma-0 mb-15' : 'ma-0 mb-1'"
        >
          <v-spacer></v-spacer>
          <v-card class="mr-2" max-width="350px" color="primary" elevation="0">
            <v-card-text class="white--text py-2">{{ message.message }}</v-card-text>
          </v-card>
        </v-row>
        
        <v-row v-else
          :class="index === context.messages.length-1 ? 'ma-0 mb-15' : 'ma-0 mb-1'"
        >
          <v-card class="ml-2 grey darken-3" max-width="350px" elevation="0">
            <template v-if="context.members.length > 2 && displayUsernameArray[index]">
              <v-card-text class="secondary--text font-weight-medium pb-0 pt-2">{{ message.user.username }}</v-card-text>
              <v-card-text class="white--text pt-0 pb-2">{{ message.message }}</v-card-text>
            </template>
            <template v-else>
              <v-card-text class="white--text py-2">{{ message.message }}</v-card-text>
            </template>
          </v-card>
        </v-row>
      </v-list-item>
      
      <v-btn v-if="checkIsDown"
        large
        icon
        bottom
        right
        absolute
        class="mr-2 mb-16 grey white--text"
        @click="scrollToBottom"
      >
        <v-icon>{{ icons.down }}</v-icon>
      </v-btn>
    </v-list>

    <v-overlay v-model="overlay" :z-index="zIndex">
      <VEmojiPicker
        v-click-outside="onClickOutsideEmojiPicker"
        class="align-center justify-center"
        @select="selectEmoji"
      ></VEmojiPicker>
    </v-overlay>
    <v-app-bar id="input-form" ref="inputForm" color="rgba(0,0,0,0)" flat>
      <v-btn icon @click="">
        <v-icon>{{ icons.attach }}</v-icon>
      </v-btn>
      <v-text-field
        v-model="message"
        class="mt-4 mx-2"
        @keyup.enter="sendMessage"
      ></v-text-field>
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
export default {
  name: 'Chat',
  components: {
    // eslint-disable-next-line vue/no-unused-components
    VEmojiPicker,
  },
  props: {
    context: {
      type: Object,
      default: null,
    },
  },
  data: () => ({
    showSettings: false,
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
    displayUsernameArray: [],
  }),
  watch: {
    async context(newVal, oldVal) {
      await this.websocket.close()
      await this.initChat()
    }
  },
  computed: {
    chatImage() {
      return 'http://localhost:8000/media/' + this.context.image
    }
  },
  created() {
    // setInterval(this.getMessages, 3000)
  },
  mounted() {
    this.initChat()
  },
  computed() {
    checkIsDown()
  },
  methods: {
    initChat() {
      this.$store.dispatch('setTheme', this.$i18n)
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
      
      if (message.message.user.id == this.$store.state.user.id) {
        this.displayUsernameArray.push(0)
      } else {
        if (this.context.messages.length == 0 || 
          message.message.user.id != this.context.messages[this.context.messages.length-1].user.id)
          this.displayUsernameArray.push(1)
        else
          this.displayUsernameArray.push(0)
      }

      this.context.messages.push(message.message)
      this.context.lastMessage = message.message.message
      
      if (
        this.$el.querySelector('#messageContainer').scrollTop ===
        this.$el.querySelector('#messageContainer').scrollTopMax
      ) {
        setTimeout(() => {
          this.scrollToBottom(), 2000
        })
      }
    },
    onError(event) {
      alert('An error occured:', event.data)
    },

    // ----------------------------------------------------
    checkIsDown() {
      return (
        this.$el.querySelector('#messageContainer').scrollTop ===
        this.$el.querySelector('#messageContainer').scrollTopMax
      )
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
        this.getUsers()
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
          // this.users = response.data.users.filter(
          //   (u) => u !== this.$store.getters.getUser.username
          // )

          this.users = []
          for (let u of response.data.users) {
            let b = 0
            for (let m of this.context.members) {
              if (u === m.username) {
                b = 1
                break
              }
            }
            if (!b)
              this.users.push(u)
          }
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

          this.context.messages = response.data.messages
          this.context.members = response.data.members
          if (response.data.messages.length != 0)
            this.context.lastMessage = response.data.messages[response.data.messages.length - 1].message

          this.displayUsernameArray = []
          for (let ind in this.context.messages) {
            if (this.context.messages[ind].user.id == this.$store.state.user.id) {
              this.displayUsernameArray.push(0)
              continue
            }
            if (ind == 0 || this.context.messages[ind].user.id != this.context.messages[ind-1].user.id)
              this.displayUsernameArray.push(1)
            else
              this.displayUsernameArray.push(0)
          }
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
      this.clearMessage()
      this.scrollToBottom()
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
    printUsers() {
      console.log(this.context.members)
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
