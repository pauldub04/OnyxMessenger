<!-- eslint-disable -->
<template>
  <v-app>
    <v-overlay :value="overlay">
      <v-progress-circular indeterminate color="primary"></v-progress-circular>
    </v-overlay>

    <v-row no-gutters>
      <NavigationDrawer
        :username="$store.state.user.username"
        :email="$store.state.user.email"
      ></NavigationDrawer>
      <v-col cols="3">
        <v-list :max-height="height" class="overflow-y-auto">
          <v-list-item-group v-model="selectedItem">
            <div v-for="(contact, index) in contacts" :key="index">
              <v-list-item class="ma-2">
                <v-list-item-content>
                  <v-list-item-title>{{ contact.title }}</v-list-item-title>
                  <v-list-item-subtitle>
                    {{ contact.lastMessage }}
                  </v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-action>
                  <v-list-item-action-text>
                    {{ contact.lastMessage.date }}
                  </v-list-item-action-text>
                </v-list-item-action>
                
              </v-list-item>
              <v-divider
                light
                v-if="index + 1 < contacts.length"
                :key="index"
              ></v-divider>
            </div>
          </v-list-item-group>
        </v-list>
        
        <v-col v-if="contacts.length == 0">
          <div class="ml-1">У вас нет чатов, cоздайте первый</div>
          <v-btn class="mt-5" to="/create-chat">Создать чат</v-btn>
        </v-col>
      </v-col>
      <v-divider vertical light></v-divider>

      <v-col>
        <Chat
          v-if="selectedItem !== undefined"
          :context="contacts[selectedItem]"
        ></Chat>
      </v-col>

    </v-row>
  </v-app>
</template>

<script>
import { mdiAccount } from '@mdi/js'
import NavigationDrawer from '~/components/NavigationDrawer'
import Chat from '~/components/Chat'
export default {
  middleware: 'auth', // check is user auth
  components: { Chat, NavigationDrawer },
  icons: { account: mdiAccount },
  data: () => ({
    selectedItem: undefined,
    contacts: [],
    overlay: true,
  }),
  beforeCreate() {
    this.$store.dispatch('middlewareAuthMain')
    this.$store.dispatch('setAuthHeader', this.$store.getters.getToken)
    console.log('set token', this.$store.getters.getToken)
  },
  updated() {
    console.log('set theme')
    this.$store.dispatch('setTheme', this.$i18n)
  },
  mounted() {
    // this.$store.dispatch('fetchUser')
    // console.log(this.$store.getters.getToken)
    this.getChats()

    this.$nextTick(function () {
      this.onResize()
    })
    window.addEventListener('resize', this.onResize)

    this.overlay = false
  },
  methods: {
    onResize() {
      this.height = window.innerHeight
    },
    countUnreadMessages(messages) {
      let counter = 0
      for (let i = messages.length - 1; i >= 0; i--) {
        if (messages[i].read) {
          break
        } else {
          counter++
        }
      }
      return counter
    },
    createChat() {
      this.$axios
        .post('http://localhost:8000/api/chats/')
        .then((response) => {
          console.log(response.data)
          this.getChats()
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getChats() {
      console.log('getChats')
      this.$axios
        .get('http://localhost:8000/api/chats/')
        .then((response) => {
          console.log(response.data)
          this.contacts = response.data.sessions
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
}
</script>

<style>
.light::-webkit-scrollbar {
  width: 15px;
}

.light::-webkit-scrollbar-track {
  background: #e6e6e6;
  border-left: 1px solid #dadada;
}

.light::-webkit-scrollbar-thumb {
  background: #b0b0b0;
  border: solid 3px #e6e6e6;
  border-radius: 7px;
}

.light::-webkit-scrollbar-thumb:hover {
  background: black;
}

.dark::-webkit-scrollbar {
  width: 15px;
}

.dark::-webkit-scrollbar-track {
  background: #202020;
  border-left: 1px solid #2c2c2c;
}

.dark::-webkit-scrollbar-thumb {
  background: #3e3e3e;
  border: solid 3px #202020;
  border-radius: 7px;
}

.dark::-webkit-scrollbar-thumb:hover {
  background: white;
}
</style>
