<script lang="ts">
	import { createEventDispatcher } from "svelte";
	import '@motion-canvas/player';
	export let elem_classes: string[] = [];
	export let value: string;
	export let visible = true;

	const dispatch = createEventDispatcher<{
		change: undefined;
		click: undefined;
	}>();

	$: value, dispatch("change");
</script>

<!-- svelte-ignore a11y-click-events-have-key-events a11y-no-static-element-interactions -->
<div
	class="prose {elem_classes.join(' ')}"
	class:hide={!visible}
	on:click={() => dispatch("click")}
>

	Debug: { value }
	{#if value}
		<motion-canvas-player
			src="{ value }"
			auto="true"
		></motion-canvas-player>
	{/if}

</div>

<style>
	.hide {
		display: none;
	}
</style>
