<template>
  <v-app>
    <v-overlay :value="overlay" opacity="1">
      <v-progress-circular indeterminate color="primary"></v-progress-circular>
    </v-overlay>

    <v-row no-gutters>
      <NavigationDrawer
        :username="$store.state.user.username"
        :email="$store.state.user.email"
      ></NavigationDrawer>
      <v-col cols="3" class="grey darken-4">
        <v-list :max-height="height" class="overflow-y-auto dark">
          <v-list-item-group v-model="selectedItem">
            <div v-for="(contact, index) in contacts" :key="index">
              <v-list-item class="ma-2" link flat>
                <v-list-item-avatar>
                  <v-badge
                    bordered
                    bottom
                    color="green"
                    dot
                    offset-x="16"
                    offset-y="9"
                  >
                    <v-avatar class="mr-2" size="30" elevation="10">
                      <v-img :src="contact.userImage" />
                    </v-avatar>
                  </v-badge>
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title>{{ contact.title }}</v-list-item-title>
                  <v-list-item-subtitle>
                    {{ contact.lastMessage }}
                  </v-list-item-subtitle>
                </v-list-item-content>
                <!-- 
                  :content="countUnreadMessages(contact.unreadMessages)"
                  :value="countUnreadMessages(contact.meunreadMessagesssages)
                 -->
                <v-list-item-action>
                  <v-badge
                    overlap
                    :content="contact.unreadMessages"
                    :value="contact.unreadMessages"
                  ></v-badge>
                  <v-list-item-action-text>{{
                    contact.lastMessage.date
                  }}</v-list-item-action-text>
                </v-list-item-action>
              </v-list-item>
              <v-divider
                v-if="index + 1 < contacts.length"
                :key="index"
              ></v-divider>
            </div>
          </v-list-item-group>
        </v-list>
        <v-col v-if="contacts.length == 0">
          <div>У вас нет чатов, cоздайте первый</div>
        </v-col>
        <v-col>
          <v-btn class="mt-2" @click="createChat">Создать чат</v-btn>
        </v-col>
      </v-col>
      <v-divider vertical></v-divider>
      <v-col>
        <Chat
          v-if="selectedItem !== -1"
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
  // middleware: 'auth', // check is user auth
  components: { Chat, NavigationDrawer },
  icons: { account: mdiAccount },
  data: () => ({
    selectedItem: -1,
    height: 0,
    contacts: [
      // {
      //   username: 'Том Хэнкс',
      //   userImage:
      //     'http://t0.gstatic.com/images?q=tbn:ANd9GcSn0EqWZ7hDt3u_M2f1KDPSdjUCLg7HCDArVAGpguedO6IlH0uIhsmh5iORmeXH',
      //   messages: [
      //     {
      //       sender_id: 1,
      //       text:
      //         'Люди всегда думают, что в любом человеке есть плохие стороны, скелеты в шкафу, демоны под кроватью. Но, правда в том, что вы никогда не узнаете всей правды обо мне, как и я о вас.',
      //       date: '13.02.2021',
      //       read: true,
      //     },
      //   ],
      //   uri: null,
      // },
      // {
      //   username: 'Джонни Депп',
      //   userImage:
      //     'http://t2.gstatic.com/images?q=tbn:ANd9GcQRmj9gO7hiNSpI6D7-3UE5ejpqfRdocu1jEEB-HIkBivMZz0GJ1-1-3mBR5Ept',
      //   messages: [
      //     {
      //       sender_id: 2,
      //       text: 'Найти себя невозможно, себя можно только создать.',
      //       date: '26.02.2021',
      //       read: false,
      //     },
      //   ],
      //   uri: null,
      // },
      // {
      //   username: 'Анджелина Джоли',
      //   userImage:
      //     'http://t2.gstatic.com/images?q=tbn:ANd9GcSlL8b-tw_kcXiljP05etQIjGWQb2pHZI1Xr2kbmRPOUc7MT66GGqhHMafG0kYy',
      //   messages: [
      //     {
      //       sender_id: 3,
      //       text:
      //         'Жизнь ничего не значит, если вы не делаете для других ничего полезного',
      //       date: '15.02.2021',
      //       read: true,
      //     },
      //   ],
      //   uri: null,
      // },
      // {
      //   username: 'Уилл Смит',
      //   userImage:
      //     'http://t2.gstatic.com/images?q=tbn:ANd9GcSY2pGlF9O0Q9ByWyUv9eAzq_UdG9vcQQCuEbNS9O-akN10LbFez2L7D3b8HQVV',
      //   messages: [
      //     {
      //       sender_id: 4,
      //       text:
      //         'Нет худшей боли, чем та, которую испытывает человек, не достигший желаемого по причине собственной лени.',
      //       date: '23.02.2021',
      //       read: false,
      //     },
      //   ],
      //   uri: null,
      // },
      // {
      //   username: 'Том Круз',
      //   userImage:
      //     'http://t1.gstatic.com/images?q=tbn:ANd9GcQV_eaB5WWobnYmnlKttxteK131L9_60iKVtQMW6PXxls0nN5G5lYtRjAW7xgrv',
      //   messages: [
      //     {
      //       sender_id: 5,
      //       text: 'Я люблю влюбляться.',
      //       date: '18.02.2021',
      //       read: true,
      //     },
      //   ],
      //   uri: null,
      // },
      // {
      //   username: 'Леонардо Ди Каприо',
      //   userImage:
      //     'http://t2.gstatic.com/images?q=tbn:ANd9GcQTZE6ZxVumFL3ga6AiETDuiRobav4wFmLjcBf9D1D85Q_B2zk5wlNlw-UrcI4f',
      //   messages: [
      //     {
      //       sender_id: 6,
      //       text:
      //         'Важно помнить: всякий раз, когда ты покупаешь что-то, ты на сто процентов поддерживаешь политику той компании, которая произвела эту вещь.',
      //       date: '18.02.2021',
      //       read: false,
      //     },
      //   ],
      //   uri: null,
      // },
      // {
      //   username: 'Мерил Стрип',
      //   userImage:
      //     'http://t0.gstatic.com/images?q=tbn:ANd9GcTlsdVtP4knLY_9DzdgKnH1tenKDPwWplRd4x-L5A5pBy228qidSgF2MAPPF0O_',
      //   messages: [
      //     {
      //       sender_id: 6,
      //       text:
      //         'Зависть — прекрасный стимул для развития творческого потенциала, которого не хватает на что-то дельное.',
      //       date: '20.09.2019',
      //       read: false,
      //     },
      //   ],
      //   uri: null,
      // },
    ],
    overlay: true,
  }),
  beforeCreate() {
    this.$store.dispatch('middlewareAuthMain')
    this.$store.dispatch('setAuthHeader', this.$store.getters.getToken)
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
      console.log('sg')
      this.$axios
        .post('http://localhost:8000/api/chats/')
        .then((response) => {
          console.log(response.data)
          this.getChats()
          // this.selectedItem = this.contacts.length - 1
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getChats() {
      console.log('kek2')
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
