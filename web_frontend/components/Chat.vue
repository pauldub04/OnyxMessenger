<template>
  <v-main>
    <v-toolbar id="info-bar" ref="infoBar" flat dark>
      <v-badge bordered bottom color="green" dot offset-x="16" offset-y="9">
        <v-avatar class="mr-2" size="40" elevation="10">
          <v-img :src="context.userImage" />
        </v-avatar>
      </v-badge>
      <v-toolbar-title class="ma-2"> {{ context.title }} </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-text-field
          v-if="inviteCount % 2 == 1"
          v-model="inviteUserName"
          class="mt-4 mr-5"
          label="Добавить пользователя"
          placeholder="Введите username"
          append-outer-icon="mdi-plus"
          clearable
          @click:append-outer="invite"
        >
        </v-text-field>
        <v-btn icon fab dark small @click="inviteCount++"
          ><v-icon>{{ icons.accountPlus }}</v-icon>
        </v-btn>
        <v-btn icon fab dark small
          ><v-icon>{{ icons.searchIcon }}</v-icon></v-btn
        >
        <v-btn icon fab dark small
          ><v-icon>{{ icons.chatInfo }}</v-icon></v-btn
        >
        <v-menu offset-y>
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
        </v-menu>
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
          <v-card class="mt-10 mr-2" max-width="350px" color="blue" dark>
            <v-list-item three-line>
              <v-list-item-content>
                <div class="mb-4">
                  {{ message.message }}
                </div>
                <v-list-item-subtitle>
                  {{ message.date }}
                </v-list-item-subtitle>
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
                  {{ message.message }}
                </div>
                <v-list-item-subtitle>
                  {{ message.date }}
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-card>
        </v-app-bar>
      </v-list-item>
      <v-btn
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
    itemsDropdownMenu: [
      { title: 'Click Me' },
      { title: 'Click Me' },
      { title: 'Click Me' },
      { title: 'Click Me 2' },
    ],
    message: '',
    inviteCount: 0,
    inviteUserName: null,
  }),
  watch: {},
  created () {
    setInterval(this.getMessages, 3000)
  },
  mounted() {
    this.getMessages()

    this.scrollToBottom();

    this.$nextTick(function () {
      this.matchHeight()
    })
    window.addEventListener('resize', this.matchHeight)
  },
  methods: {
    scrollToBottom() {
      const container = this.$el.querySelector("#messageContainer");
      container.scrollTop = container.scrollHeight;
    },
    invite() {
      if (this.inviteUserName !== null) {
        console.log(this.inviteUserName)

        this.$axios
          .patch(`http://127.0.0.1:8000/api/chats/${this.context.uri}/`, {
            username: this.inviteUserName
          })
          .then((response) => {
            console.log(response.data)
            alert(response.data.message)
          })
          .catch((error) => {
            console.log(error)
          })

        this.inviteCount++
      }
    },
    updateFile(file) {
      this.files.push(file)
      console.log("File in files!")
    },
    getMessages() {
      this.$axios
        .get(`http://localhost:8000/api/chats/${this.context.uri}/messages/`)
        .then((response) => {
          console.log(response.data)

          this.context.messages = response.data.messages
          if (response.data.messages.length != 0)
            this.context.lastMessage = response.data.messages[response.data.messages.length - 1].message
          console.log(this.context.messages)
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
      if (this.message == null || this.message == '')
        return
      this.$axios
        .post(`http://localhost:8000/api/chats/${this.context.uri}/messages/`, {
          message: this.message,
        })
        .then((response) => {
          console.log(response.data)
          this.getMessages()
        })
        .catch((error) => {
          console.log(error)
        })
      this.clearMessage()
      this.scrollToBottom();
    },
    makeAudioMessage() {
      alert('Audio done!')
    },
    selectEmoji(emoji) {
      this.overlay = false
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
