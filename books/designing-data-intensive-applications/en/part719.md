6.  Once the coordinator’s decision has been written to disk, the commit or abort request is sent
to all participants. If this request fails or times out, the coordinator must retry forever until
it succeeds. There is no more going back: if the decision was to commit, that decision must be
enforced, no matter how many retries it takes. If a participant has crashed in the meantime, the
transaction will be committed when it recovers—since the participant voted “yes,” it cannot
refuse to commit when it recovers. Thus, the protocol contains two crucial “points of no return”: when a participant votes “yes,” it
promises that it will definitely be able to commit later (although the coordinator may still choose to
abort); and once the coordinator decides, that decision is irrevocable. Those promises ensure the
atomicity of 2PC. (Single-node atomic commit lumps these two events into one: writing the commit
record to the transaction log.)