<template>
  <main class="flex flex-col p-2">
    <div
      class="flex gap-2"
      :class="[ui.isMaximized ? 'overflow-x-auto' : null]"
    >
      <KelasEmboots
        title="Bit Spark"
        badge="Beginner Level"
        :backgroundImage="ImgBitSpark"
        :features="[
          'Dasar Elektronika & Logika Digital',
          'Pengenalan GPIO & LED Blinking',
          'Setup STM32CubeIDE',
          'Push Button & Debouncing',
          'Mini Project: LED Controller',
        ]"
      />
      <KelasEmboots
        title="Bit Explorer"
        badge="Foundation Level"
        :backgroundImage="ImgBitExplorer"
        :features="[
          'Timer & PWM Dasar',
          'Interrupt (EXTI & Timer)',
          'ADC & Sensor Analog',
          'UART Communication',
          'Mini Project: Sensor Monitoring System',
        ]"
      />
      <KelasEmboots
        title="Bit Apprentice"
        badge="Intermediate Level"
        :backgroundImage="ImgBitApprentice"
        :features="[
          'I2C & SPI Communication',
          'EEPROM & External Device Interface',
          'State Machine Implementation',
          'Memory & Register Level Programming (LL)',
          'Mini Project: Multi-Sensor Embedded System',
        ]"
      />
      <KelasEmboots
        title="Bit Ranger"
        badge="Advanced Level"
        :backgroundImage="ImgBitRanger"
        :features="[
          'RTOS (FreeRTOS) Fundamentals',
          'Task Scheduling & Synchronization',
          'DMA & Performance Optimization',
          'Embedded Debugging & Profiling',
          'Final Project: Real-World Embedded System',
        ]"
      />
    </div>
  </main>
</template>

<script setup lang="ts">
import KelasEmboots from "@/components/Home/KelasEmboots.vue";
import ImgBitSpark from "@/assets/kelas/img1.png";
import ImgBitExplorer from "@/assets/kelas/img1.png";
import ImgBitApprentice from "@/assets/kelas/img1.png";
import ImgBitRanger from "@/assets/kelas/img1.png";
import { useUIStore } from "@/stores/ui";
const ui = useUIStore();
</script>

<style scoped></style>
