<template>
  <v-navigation-drawer permanent expand-on-hover>
    <v-list>
      <v-list-item :to="localePath('/main')" inactive>
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
      <v-list-item :to="localePath('/main')">
        <v-list-item-icon>
          <v-icon> mdi-message-outline </v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>
            {{ $t('pages.NavigationDrawer.chats') }}
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item :to="localePath('/settings')">
        <v-list-item-icon>
          <v-icon> mdi-cog </v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>
            {{ $t('pages.NavigationDrawer.settings') }}
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item :to="localePath('/create-chat')">
        <v-list-item-icon>
          <v-icon> mdi-message-text </v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>
            {{ $t('pages.NavigationDrawer.createChat') }}
          </v-list-item-title>
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
          <v-list-item-title>{{
            $t('pages.NavigationDrawer.logOut')
          }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 'NavigationDrawer',
  props: {
    username: {
      type: String,
      default: 'username',
    },
    email: {
      type: String,
      default: 'email',
    },
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
}
</script>

<style scoped></style>
