---
name: layer-map
description: "My layer map: process → runtime → syscall → kernel → wire → remote, plus orchestrator / control plane / data store, and who owns which state. Every new concept gets placed here first. Built by me in a lab; Claude reviews."
metadata:
  type: reference
---

# Layer map

Why this exists: many repeated mistakes are wrong-layer mistakes (placing the TCP handshake between a syscall and the kernel, expecting syscalls in a packet capture, blaming the app for a key the terminal multiplexer swallowed). Patching each instance does not stop them; one frame might.

Fill it in a lab: Claude walks one request through every layer as a worked example, I complete the table, then I place three new concepts alone.

| Layer | What lives here | Who owns the state | Instrument that sees it | Easy to confuse with |
|---|---|---|---|---|
| process (my code) | | | | |
| runtime / library | | | | |
| syscall boundary | | | | |
| kernel (sockets, buffers, fds, scheduler) | | | | |
| wire (packets, handshake) | | | | |
| remote host | | | | |
| orchestrator (Kubernetes, tmux server) | | | | |
| control plane (cloud API, Terraform, identity provider) | | | | |
| data store (database, caches) | | | | |
