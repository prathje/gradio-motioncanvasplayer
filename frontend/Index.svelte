<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import MCPlayer from "./shared/MCPlayer.svelte";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";
	import { Block, BlockLabel } from "@gradio/atoms";
	import { Code as CodeIcon } from "@gradio/icons";

	export let label = "Motion Canvas Player";
	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let loading_status: LoadingStatus;
	export let gradio: Gradio<{
		change: never;
		click: never;
		clear_status: LoadingStatus;
	}>;
	export let show_label = false;
	export let min_height: number | undefined = undefined;
	export let max_height: number | undefined = undefined;
	export let container = false;
	export let padding = true;
	export let value = "";

	export let auto: bool | undefined = undefined;
	export let quality: number | undefined = undefined;
	export let width: int | undefined = undefined;
	export let height: int | undefined = undefined;
	export let variables: str | undefined = undefined;
</script>

<Block {visible} {elem_id} {elem_classes} {container} padding={false}>
	{#if show_label}
		<BlockLabel Icon={CodeIcon} {show_label} {label} float={false} />
	{/if}

	<StatusTracker
		autoscroll={gradio.autoscroll}
		i18n={gradio.i18n}
		{...loading_status}
		variant="center"
		on:clear_status={() => gradio.dispatch("clear_status", loading_status)}
	/>
	<div
		class="html-container"
		class:padding
		class:pending={loading_status?.status === "pending"}
		style:min-height={min_height && loading_status?.status !== "pending"
			? css_units(min_height)
			: undefined}
		style:max-height={max_height ? css_units(max_height) : undefined}
	>
		<MCPlayer
			min_height={loading_status && loading_status?.status !== "complete"}
			{value}
			{auto}
			{quality}
			{width}
			{height}
			{variables}
			
			{elem_classes}
			{visible}
			on:change={() => gradio.dispatch("change")}
			on:click={() => gradio.dispatch("click")}
		/>
	</div>
</Block>

<style>
	.padding {
		padding: var(--block-padding);
	}

	div {
		transition: 150ms;
	}

	.pending {
		opacity: 0.2;
	}
</style>
