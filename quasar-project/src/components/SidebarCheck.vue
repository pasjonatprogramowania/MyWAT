<template>
  <div class="q-pa-lg">
    <q-list bordered class="rounded-borders">
      <q-expansion-item
        expand-separator
        icon="perm_identity"
        label="Typ wydarzenia"
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
      <q-btn
        color="primary"
        text-color="white"
        label="Dodaj"
        @click="emit('addPoint')"
      />
      <q-btn
        color="primary"
        text-color="white"
        label="Usuń"
        @click="emit('removePoint')"
      />
      <q-btn
        color="primary"
        text-color="white"
        label="Popraw"
        @click="emit('correctPoint')"
      />
    </q-expansion-item>
    <q-expansion-item expand-separator icon="signal_wifi_off" label="Przejazdy">
      <TimeInput></TimeInput>
      <q-btn color="primary" text-color="white" label="Pokaż" />
    </q-expansion-item>
  </div>
</template>

<script setup>
import { ref, defineEmits } from "vue";
import TimeInput from "components/TimeInput.vue";

const emit = defineEmits(["addPoint", "removePoint", "correctPoint"]);
const group = ref(["kz"]);

const options = ref([
  {
    label: "Koła zainteresowań ",
    value: "kz",
  },
  {
    label: "Imprezy eventy watowe",
    value: "iw",
  },
  {
    label: "Ogłoszenia",
    value: "og",
  },
]);
</script>
