<template>
  <v-main>
    <v-toolbar id="info-bar" ref="infoBar" flat dark>
      <v-badge bordered bottom color="green" dot offset-x="16" offset-y="9">
        <v-avatar class="mr-2" size="40" elevation="10">
          <v-img :src="context.userImage" />
        </v-avatar>
      </v-badge>
      <v-toolbar-title class="ma-2"> {{ context.username }} </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
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
    <v-list :height="height" class="overflow-y-auto dark">
      <v-list-item v-for="(message, index) in context.messages" :key="index">
        <v-app-bar
          v-if="message.id_sender === user_id"
          color="rgba(0,0,0,0)"
          flat
          class="mt-15"
        >
          <v-spacer></v-spacer>
          <v-card class="mt-10 mr-2" max-width="350px" color="blue" dark>
            <v-list-item three-line>
              <v-list-item-content>
                <div class="mb-4">
                  {{ message.text }}
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
        <v-app-bar v-else color="rgba(0,0,0,0)" flat class="mt-15">
          <v-badge bordered bottom color="green" dot offset-x="16" offset-y="9">
            <v-avatar class="mt-n5 mr-2" size="30" elevation="10">
              <v-img :src="context.userImage" />
            </v-avatar>
          </v-badge>
          <v-card class="mt-10" max-width="350px" color="grey">
            <v-list-item three-line>
              <v-list-item-content>
                <div class="mb-4">
                  {{ message.text }}
                </div>
                <v-list-item-subtitle>
                  {{ message.date }}
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-card>
        </v-app-bar>
      </v-list-item>
    </v-list>
    <v-divider></v-divider>
    <v-toolbar id="input-form" ref="inputForm" flat>
      <v-btn icon fab dark small>
        <v-icon>{{ icons.attach }}</v-icon>
      </v-btn>
      <v-container fluid>
        <v-textarea
          flat
          class="pt-6"
          no-resize
          rows="1"
          placeholder="Type your message..."
        ></v-textarea>
      </v-container>
      <v-toolbar-items>
        <v-btn icon fab dark small
          ><v-icon>{{ icons.send }}</v-icon></v-btn
        >
        <v-btn icon fab dark small
          ><v-icon>{{ icons.smile }}</v-icon></v-btn
        >
        <v-btn icon fab dark small
          ><v-icon>{{ icons.micro }}</v-icon></v-btn
        >
      </v-toolbar-items>
    </v-toolbar>
  </v-main>
</template>

<script>
import {
  mdiMagnify,
  mdiPageLayoutSidebarRight,
  mdiDotsVertical,
  mdiPaperclip,
  mdiEmoticonHappyOutline,
  mdiMicrophoneOutline,
  mdiSend,
} from '@mdi/js'
export default {
  name: 'Chat',
  props: {
    context: {
      type: Array,
      default: null,
    },
  },
  data: () => ({
    user_id: 1,
    height: 0,
    icons: {
      searchIcon: mdiMagnify,
      chatInfo: mdiPageLayoutSidebarRight,
      extraInfo: mdiDotsVertical,
      attach: mdiPaperclip,
      smile: mdiEmoticonHappyOutline,
      micro: mdiMicrophoneOutline,
      send: mdiSend,
    },
    itemsDropdownMenu: [
      { title: 'Click Me' },
      { title: 'Click Me' },
      { title: 'Click Me' },
      { title: 'Click Me 2' },
    ],
  }),
  mounted() {
    this.$nextTick(function () {
      this.matchHeight()
    })
    window.addEventListener('resize', this.matchHeight)
  },
  methods: {
    matchHeight() {
      const heightInfobar = document.getElementById('info-bar').offsetHeight
      const heightForm = document.getElementById('input-form').offsetHeight
      const windowHeight = window.innerHeight
      this.height = windowHeight - (heightInfobar + heightForm) - 2
    },
  },
}
</script>

<style scoped></style>
