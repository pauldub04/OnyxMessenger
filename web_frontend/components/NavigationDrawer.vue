<template>
  <v-navigation-drawer permanent expand-on-hover>
    <v-list>
      <v-list-item class="px-2">
        <v-list-item-avatar>
          <v-badge bordered bottom color="green" dot offset-x="16" offset-y="9">
            <v-avatar class="mr-2" size="33" elevation="10">
              <!-- <v-img src="https://randomuser.me/api/portraits/women/85.jpg" /> -->
            </v-avatar>
          </v-badge>
        </v-list-item-avatar>
      </v-list-item>

      <v-list-item link>
        <v-list-item-content>
          <v-list-item-title class="title">{{ username }}</v-list-item-title>
          <v-list-item-subtitle>{{ email }}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-divider></v-divider>
    <v-list dense>
      <!-- <v-list-item
        v-for="item in items"
        :key="item.title"
        class="mb-2"
        link
      >
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.label }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item> -->
      <v-list-item link>
        <v-list-item-icon>
          <v-icon> mdi-cog </v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title> Настройки </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item to="/create-chat">
        <v-list-item-icon>
          <v-icon> mdi-message-text </v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title> Создать чат </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-spacer></v-spacer>
    <v-list dense>
      <v-list-item link @click="$store.dispatch('logOut')">
        <v-list-item-icon>
          <v-icon>mdi-logout</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Выйти из системы</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 'NavigationDrawer',
  props: {
    username: String,
    email: String,
  },
  data() {
    return {
      items: [
        { label: 'Настройки', icon: 'mdi-cog', link: '/settings' },
        {
          label: 'Создать чат',
          icon: 'mdi-message-text',
          link: '/create-chat',
        },
      ],
    }
  },
  methods: {
    click() {
      console.log('df')
      this.$nuxt.$emit('createChat')
    },
  },
}
</script>

<style scoped></style>
