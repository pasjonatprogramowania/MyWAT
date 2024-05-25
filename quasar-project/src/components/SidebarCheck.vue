<template>
  <div class="q-pa-lg">
    <q-list bordered class="rounded-borders">
      <q-expansion-item
        expand-separator
        icon="perm_identity"
        label="Account settings"
        caption="Filtry"
      >
      <q-option-group
        v-model="group"
        :options="options"
        color="primary"
        type="checkbox"
      />
      </q-expansion-item>
     </q-list>
    <q-expansion-item
      expand-separator
      icon="signal_wifi_off"
      label="Dodawanie punktów"
    >
      <q-btn color="primary" text-color="white" label="Dodaj" />
      <q-btn color="primary" text-color="white" label="Usuń" />
      <q-btn color="primary" text-color="white" label="Popraw" />
    </q-expansion-item>
    <q-expansion-item
      expand-separator
      icon="signal_wifi_off"
      label="Przejazdy"
    >
      <TimeInput></TimeInput>
      <q-btn color="primary" text-color="white" label="Pokaż" />
      </q-expansion-item>
  </div>
</template>

<script>
import { ref } from 'vue'
import TimeInput from "components/TimeInput.vue";

export default {
  components: {TimeInput},
  setup () {
    return {
      group: ref(['op1']),

      options: [
        {
          label: 'Kołka zainteresowanie ',
          value: 'kz'
        },
        {
          label: 'Imprezy eventy watowe',
          value: 'iw'
        },
        {
          label: 'Ogłoszenia',
          value: 'og'
        },

      ]
    }
  }
}
</script>
