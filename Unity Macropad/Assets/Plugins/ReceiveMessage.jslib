mergeInto(LibraryManager.library, { _SendMessage: function(id, msg, x, y) { ReceiveMessage(id, msg, x, y); } });