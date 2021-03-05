<template>
  <v-app>
    <v-row no-gutters>
      <NavigationDrawer></NavigationDrawer>
      <v-col cols="3" class="grey darken-4">
        <v-virtual-scroll
          :items="contacts"
          :height="windowSize.y"
          item-height="80"
        >
          <template v-slot:default="{ item }">
            <v-list-item class="ma-2" link>
              <v-list-item-avatar
                ><v-img :src="item.userImage"></v-img
              ></v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title>{{ item.username }}</v-list-item-title>
                <v-list-item-subtitle>{{
                  item.lastMessage
                }}</v-list-item-subtitle>
              </v-list-item-content>
              <v-list-item-action>
                <v-badge
                  overlap
                  :content="item.unreadMessages"
                  :value="item.unreadMessages"
                ></v-badge>
                <v-list-item-action-text>{{
                  item.dateLastMessage
                }}</v-list-item-action-text>
              </v-list-item-action>
            </v-list-item>
            <v-divider inset></v-divider>
          </template>
        </v-virtual-scroll>
      </v-col>
      <v-col>
        <p></p>
      </v-col>
    </v-row>
  </v-app>
</template>

<script>
import NavigationDrawer from '~/components/NavigationDrawer'
export default {
  components: { NavigationDrawer },
  data() {
    return {
      windowSize: {
        x: 0,
        y: 0,
      },
      contacts: [
        {
          id: 1,
          username: 'Том Хэнкс',
          userImage:
            'http://t0.gstatic.com/images?q=tbn:ANd9GcSn0EqWZ7hDt3u_M2f1KDPSdjUCLg7HCDArVAGpguedO6IlH0uIhsmh5iORmeXH',
          lastMessage:
            'Люди всегда думают, что в любом человеке есть плохие стороны, скелеты в шкафу, демоны под кроватью. Но, правда в том, что вы никогда не узнаете всей правды обо мне, как и я о вас.',
          dateLastMessage: '13.02.2021',
          unreadMessages: 1,
        },
        {
          id: 2,
          username: 'Джонни Депп',
          userImage:
            'http://t2.gstatic.com/images?q=tbn:ANd9GcQRmj9gO7hiNSpI6D7-3UE5ejpqfRdocu1jEEB-HIkBivMZz0GJ1-1-3mBR5Ept',
          lastMessage: 'Найти себя невозможно, себя можно только создать.',
          dateLastMessage: '26.02.2021',
          unreadMessages: 5,
        },
        {
          id: 3,
          username: 'Анджелина Джоли',
          userImage:
            'http://t2.gstatic.com/images?q=tbn:ANd9GcSlL8b-tw_kcXiljP05etQIjGWQb2pHZI1Xr2kbmRPOUc7MT66GGqhHMafG0kYy',
          lastMessage:
            'Жизнь ничего не значит, если вы не делаете для других ничего полезного',
          dateLastMessage: '15.02.2021',
          unreadMessages: 0,
        },
        {
          id: 4,
          username: 'Уилл Смит',
          userImage:
            'http://t2.gstatic.com/images?q=tbn:ANd9GcSY2pGlF9O0Q9ByWyUv9eAzq_UdG9vcQQCuEbNS9O-akN10LbFez2L7D3b8HQVV',
          lastMessage:
            'Нет худшей боли, чем та, которую испытывает человек, не достигший желаемого по причине собственной лени.',
          dateLastMessage: '23.02.2021',
          unreadMessages: 8,
        },
        {
          id: 5,
          username: 'Том Круз',
          userImage:
            'http://t1.gstatic.com/images?q=tbn:ANd9GcQV_eaB5WWobnYmnlKttxteK131L9_60iKVtQMW6PXxls0nN5G5lYtRjAW7xgrv',
          lastMessage: 'Я люблю влюбляться.',
          dateLastMessage: '18.02.2021',
          unreadMessages: 0,
        },
        {
          id: 6,
          username: 'Леонардо Ди Каприо',
          userImage:
            'http://t2.gstatic.com/images?q=tbn:ANd9GcQTZE6ZxVumFL3ga6AiETDuiRobav4wFmLjcBf9D1D85Q_B2zk5wlNlw-UrcI4f',
          lastMessage:
            'Важно помнить: всякий раз, когда ты покупаешь что-то, ты на сто процентов поддерживаешь политику той компании, которая произвела эту вещь.',
          dateLastMessage: '18.02.2021',
          unreadMessages: 2,
        },
        {
          id: 7,
          username: 'Мерил Стрип',
          userImage:
            'http://t0.gstatic.com/images?q=tbn:ANd9GcTlsdVtP4knLY_9DzdgKnH1tenKDPwWplRd4x-L5A5pBy228qidSgF2MAPPF0O_',
          lastMessage:
            'Зависть — прекрасный стимул для развития творческого потенциала, которого не хватает на что-то дельное.',
          dateLastMessage: '20.09.2019',
          unreadMessages: 20,
        },
      ],
    }
  },
  mounted() {
    this.onResize()
  },
  methods: {
    onResize() {
      this.windowSize = { x: window.innerWidth, y: window.innerHeight }
    },
  },
}
</script>

<style></style>
