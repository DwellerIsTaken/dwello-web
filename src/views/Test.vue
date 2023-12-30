<script setup lang="ts">

import { ref } from 'vue'

import { usePotiah, ScrollView, ScrollComponent } from 'potiah'

const flag = ref(true)
const duration = ref(1.4)

const { scrollTo, potiah, direction, isScrolling } = usePotiah()

const zero = ref<InstanceType<typeof ScrollComponent> | null>(null)
const zero1 = ref<InstanceType<typeof ScrollComponent> | null>(null)
const blank = ref<HTMLElement>()

</script>


<template>  
  <main>
    <ScrollView :duration="duration" css-direction root>
      <ScrollComponent id="top" is="section" class="zero" ref="zero">
        Scroll comp text!!!
      </ScrollComponent>
      <div class="hello">
        <h1>Hello World From Sam</h1>
      </div>

      <div id="sticky" class="second" data-scroll data-scroll-speed="0.2" :data-flag="flag">
        <h1
          data-scroll
          data-scroll-sticky
          data-scroll-target="#sticky"
        >
          Sticky scroll example
        </h1>
        <p>Placeholders Placeholders</p>
        <p>Placeholders Placeholders</p>
        <p>Placeholders Placeholders</p>
        <p>Placeholders Placeholders</p>
      </div>

      <div class="third">
        <h1>Vertical Parallax scroll</h1>
        <h1>Horizontal Parallax Scroll</h1>
      </div>
      <div id="blank" class="blank" ref="blank"></div>
      <!--<section className="scroll-into-view" data-scroll-section>
        <h1>
          Here, we're calling the Animate class when the Content scrolls into view
        </h1>
      </section>-->
      <ScrollComponent
        in-view-class="test-in-view-class"
        repeat
        :style="{ height: '25vh', background: 'blue' }"
      >dirty bastard </ScrollComponent>
    </ScrollView>
  </main>
</template>

<script>
</script>

<style>
section {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: xx-large;
}
.hello {
  background-color: red;
  width: 100vw;
  background-image: url("/src/assets/background.png");
  background-size: cover;
  color: rgba(0, 0, 0, 0.745);
}
.third {
  background-color: greenyellow;
}
#sticky {
  background-color: black;
  padding: 50px;
}
.scroll-into-view {
  background-color: black;
  color: white;
}
</style>